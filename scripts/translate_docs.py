#!/usr/bin/env python3
import argparse
import json
import re
import time
from pathlib import Path

from deep_translator import GoogleTranslator, MyMemoryTranslator
from deep_translator.exceptions import TranslationNotFound


ROOT = Path(__file__).resolve().parent.parent
ZH_ROOT = ROOT / "zh-CN"
EXCLUDED_DIRS = {"zh-CN", "docs-en", "build", "node_modules", ".git"}

TITLE_OVERRIDES = {
    "The Pragmatic Programmer": "程序员修炼之道",
    "Foreword": "前言",
    "Preface to the First Edition": "第一版序言",
    "Preface to the Second Edition": "第二版序言",
    "From the Preface to the First Edition": "第一版序摘录",
    "1. A Pragmatic Philosophy": "1. 务实的哲学",
    "2. A Pragmatic Approach": "2. 务实的方法",
    "3. The Basic Tools": "3. 基础工具",
    "4. Pragmatic Paranoia": "4. 务实的偏执",
    "5. Bend, or Break": "5. 弯而不折",
    "6. Concurrency": "6. 并发",
    "7. While You Are Coding": "7. 编码之时",
    "8. Before the Project": "8. 项目启动前",
    "9. Pragmatic Projects": "9. 务实的项目",
    "10. Postface": "10. 后记",
    "A1. Bibliography": "A1. 参考书目",
    "A2. Possible Answers to the Exercises": "A2. 练习题参考答案",
    "Chapter 1 - A Pragmatic Philosophy": "第 1 章 - 务实的哲学",
    "Chapter 2 - A Pragmatic Approach": "第 2 章 - 务实的方法",
    "Chapter 3 - The Basic Tools": "第 3 章 - 基础工具",
    "Chapter 4 - Pragmatic Paranoia": "第 4 章 - 务实的偏执",
    "Chapter 5 - Bend, or Break": "第 5 章 - 弯而不折",
    "Chapter 6 - Concurrency": "第 6 章 - 并发",
    "Chapter 7 - While You Are Coding": "第 7 章 - 编码之时",
    "Chapter 8 - Before the Project": "第 8 章 - 项目启动前",
    "Chapter 9 - Pragmatic Projects": "第 9 章 - 务实的项目",
    "Chapter 10 - Postface": "第 10 章 - 后记",
    "Appendix 2 - Possible Answers to the Exercises": "附录 2 - 练习题参考答案",
    "Topic 1. It's Your Life": "主题 1. 这是你的人生",
    "Topic 2. The Cat Ate My Source Code": "主题 2. 猫吃掉了我的源码",
    "Topic 3. Software Entropy": "主题 3. 软件熵",
    "Topic 4. Stone Soup and Boiled Frogs": "主题 4. 石头汤与温水煮青蛙",
    "Topic 5. Good-Enough Software": "主题 5. 足够好的软件",
    "Topic 6. Your Knowledge Portfolio": "主题 6. 你的知识资产组合",
    "Topic 7. Communicate!": "主题 7. 沟通！",
    "Topic 8. The Essence of Good Design": "主题 8. 优秀设计的本质",
    "Topic 9. DRY - The Evils of Duplication": "主题 9. DRY：重复之恶",
    "Topic 10. Orthogonality": "主题 10. 正交性",
    "Topic 11. Reversibility": "主题 11. 可逆性",
    "Topic 12. Tracer Bullets": "主题 12. 曳光弹",
    "Topic 13. Prototypes and Post-it Notes": "主题 13. 原型与便利贴",
    "Topic 14. Domain Languages": "主题 14. 领域语言",
    "Topic 15. Estimating": "主题 15. 估算",
    "Topic 16. The Power of Plain Text": "主题 16. 纯文本的力量",
    "Topic 17. Shell Games": "主题 17. Shell 把戏",
    "Topic 18. Power Editing": "主题 18. 强力编辑",
    "Topic 19. Version Control": "主题 19. 版本控制",
    "Topic 20. Debugging": "主题 20. 调试",
    "Topic 21. Text Manipulation": "主题 21. 文本处理",
    "Topic 22. Engineering Daybooks": "主题 22. 工程日志",
    "Topic 23. Design by Contract": "主题 23. 契约式设计",
    "Topic 24. Dead Programs Tell No Lies": "主题 24. 死掉的程序不会说谎",
    "Topic 25. Assertive Programming": "主题 25. 自信式编程",
    "Topic 26. How to Balance Resources": "主题 26. 如何平衡资源",
    "Topic 27. Don't Outrun Your Headlights": "主题 27. 别跑得比车灯照得还远",
    "Topic 28. Decoupling": "主题 28. 解耦",
    "Topic 29. Juggling the Real World": "主题 29. 应对真实世界",
    "Topic 30. Transforming Programming": "主题 30. 变换式编程",
    "Topic 31. Inheritance Tax": "主题 31. 继承税",
    "Topic 32. Configuration": "主题 32. 配置",
    "Topic 33. Breaking Temporal Coupling": "主题 33. 打破时间耦合",
    "Topic 34. Shared State Is Incorrect State": "主题 34. 共享状态就是错误状态",
    "Topic 35. Actors and Processes": "主题 35. Actor 与进程",
    "Topic 36. Blackboards": "主题 36. 黑板系统",
    "Topic 37. Listen to Your Lizard Brain": "主题 37. 倾听你的蜥蜴脑",
    "Topic 38. Programming by Coincidence": "主题 38. 凭巧编程",
    "Topic 39. Algorithm Speed": "主题 39. 算法速度",
    "Topic 40. Refactoring": "主题 40. 重构",
    "Topic 41. Test to Code": "主题 41. 用测试来思考代码",
    "Topic 42. Property-Based Testing": "主题 42. 基于性质的测试",
    "Topic 43. Stay Safe Out There": "主题 43. 在外务必注意安全",
    "Topic 44. Naming Things": "主题 44. 命名之道",
    "Topic 45. The Requirements Pit": "主题 45. 需求陷阱",
    "Topic 46. Solving Impossible Puzzles": "主题 46. 破解不可能的谜题",
    "Topic 47. Working Together": "主题 47. 协作共事",
    "Topic 48. The Essence of Agility": "主题 48. 敏捷的本质",
    "Topic 49. Pragmatic Teams": "主题 49. 务实的团队",
    "Topic 50. Coconuts Don't Cut It": "主题 50. 只靠椰子可不行",
    "Topic 51. Pragmatic Starter Kit": "主题 51. 务实的起步工具包",
    "Topic 52. Delight Your Users": "主题 52. 让用户感到愉悦",
    "Topic 53. Pride and Prejudice": "主题 53. 傲慢与偏见",
    "What's in a Name": "名字里有什么",
    "How the Book Is Organized": "本书如何组织",
    "Source Code and Other Resources": "源代码与其他资源",
    "Send Us Feedback": "欢迎反馈",
    "Second Edition Acknowledgments": "第二版致谢",
    "Who Should Read This Book": "谁应该读这本书",
    "What Makes a Pragmatic Programmer": "什么造就了务实的程序员",
    "Individual Pragmatists, Large Teams": "个体的务实者与大型团队",
    "It's a Continuous Process": "这是一个持续不断的过程",
    "## Topics": "## 主题",
    "## Chapters": "## 章节",
}

PROTECTED_TERMS = [
    "DRY",
    "DAMP",
    "NIST",
    "ASCII",
    "Unicode",
    "API",
    "HTTP",
    "HTTPS",
    "URL",
    "URLs",
    "UTF-8",
    "JSON",
    "YAML",
    "XML",
    "Markdown",
    "HTML",
    "CSS",
    "JavaScript",
    "TypeScript",
    "Node.js",
    "Git",
    "GitHub",
    "README",
    "Docusaurus",
    "Actor",
    "Actors",
]

translator = GoogleTranslator(source="en", target="zh-CN")
fallback_translator = MyMemoryTranslator(source="en-US", target="zh-CN")
cache = {}
PHRASE_OVERRIDES = {
    "Start coding.": "开始编码。",
}


def english_docs():
    for path in sorted(ROOT.rglob("*.md")):
        if any(part in EXCLUDED_DIRS for part in path.relative_to(ROOT).parts):
            continue
        yield path


def protect_terms(text):
    replacements = {}
    protected = text
    for index, term in enumerate(PROTECTED_TERMS):
        token = f"<zterm{index}/>"
        if term in protected:
            protected = protected.replace(term, token)
            replacements[token] = term
    return protected, replacements


def restore_terms(text, replacements):
    restored = text
    for token, original in replacements.items():
        restored = restored.replace(token, original)
    return restored


def translate_plain_text(text):
    stripped = text.strip()
    if not stripped:
        return text
    if stripped in TITLE_OVERRIDES:
        translated = TITLE_OVERRIDES[stripped]
        return text.replace(stripped, translated)
    if stripped in PHRASE_OVERRIDES:
        translated = PHRASE_OVERRIDES[stripped]
        return text.replace(stripped, translated)
    if stripped in cache:
        translated = cache[stripped]
        return text.replace(stripped, translated)

    protected, replacements = protect_terms(stripped)
    try:
        translated = translator.translate(protected)
    except Exception:
        time.sleep(1.0)
        try:
            translated = translator.translate(protected)
        except Exception:
            try:
                translated = fallback_translator.translate(protected)
            except TranslationNotFound:
                translated = protected
            except Exception:
                translated = protected
    if translated is None:
        translated = protected
    translated = restore_terms(translated, replacements)
    translated = translated.replace("## 主题", "## 主题")
    translated = translated.replace("## 章节", "## 章节")
    translated = translated.replace("《实用程序员》", "《程序员修炼之道》")
    cache[stripped] = translated
    time.sleep(0.02)
    return text.replace(stripped, translated)


INLINE_CODE_RE = re.compile(r"`[^`]+`")
AUTO_LINK_RE = re.compile(r"<https?://[^>]+>")
MD_LINK_RE = re.compile(r"(!?)\[((?:[^\[\]]+|\[[^\]]*\])*)\]\((<[^>]+>|[^)]+)\)")


def mask_patterns(text):
    replacements = {}
    masked = text

    def do_mask(pattern, value_transform=None):
        nonlocal masked
        items = list(pattern.finditer(masked))
        for offset, match in enumerate(items):
            original = match.group(0)
            replacement = value_transform(match) if value_transform else original
            token = f"<zmask{len(replacements)}/>"
            masked = masked.replace(original, token, 1)
            replacements[token] = replacement

    def link_transform(match):
        bang, label, target = match.groups()
        if bang:
            return match.group(0)
        translated_label = translate_inline(label)
        return f"[{translated_label}]({target})"

    do_mask(AUTO_LINK_RE)
    do_mask(INLINE_CODE_RE)
    do_mask(MD_LINK_RE, link_transform)
    return masked, replacements


def unmask(text, replacements):
    restored = text
    for token, original in replacements.items():
        restored = restored.replace(token, original)
    return restored


def normalize_link_targets(source_text, translated_text):
    source_matches = list(MD_LINK_RE.finditer(source_text))
    translated_matches = list(MD_LINK_RE.finditer(translated_text))
    if len(source_matches) != len(translated_matches):
        return translated_text

    rebuilt = []
    cursor = 0
    for source_match, translated_match in zip(source_matches, translated_matches):
        rebuilt.append(translated_text[cursor:translated_match.start()])
        bang = translated_match.group(1)
        label = translated_match.group(2)
        target = source_match.group(3)
        rebuilt.append(f"{bang}[{label}]({target})")
        cursor = translated_match.end()
    rebuilt.append(translated_text[cursor:])
    return "".join(rebuilt)


def translate_inline(text):
    stripped = text.strip()
    if not stripped:
        return text
    if stripped in TITLE_OVERRIDES:
        return text.replace(stripped, TITLE_OVERRIDES[stripped])
    masked, replacements = mask_patterns(text)
    translated = translate_plain_text(masked)
    return unmask(translated, replacements)


def translate_heading(line):
    match = re.match(r"^(#{1,6}\s+)(.*)$", line)
    if not match:
        return line
    prefix, body = match.groups()
    return prefix + translate_inline(body)


def translate_list_item(block):
    match = re.match(r"^(\s*(?:[-*]|\d+\.)\s+)([\s\S]*)$", block)
    if not match:
        return translate_inline(block)
    prefix, body = match.groups()
    body = re.sub(r"\s*\n\s*", " ", body).strip()
    return prefix + translate_inline(body)


def translate_blockquote(block):
    lines = [re.sub(r"^\s*>\s?", "", line) for line in block.splitlines()]
    body = "\n".join(lines).strip()
    translated = translate_inline(body)
    return "\n".join("> " + line if line else ">" for line in translated.splitlines())


def translate_paragraph(block):
    body = re.sub(r"\s*\n\s*", " ", block).strip()
    return translate_inline(body)


def translate_table(block_lines):
    translated = []
    for line in block_lines:
        if re.match(r"^\|\s*[-: ]+\|\s*$", line) or re.match(r"^\|(?:\s*[-: ]+\|)+\s*$", line):
            translated.append(line)
            continue

        pieces = line.split("|")
        if len(pieces) < 3:
            translated.append(line)
            continue

        cells = []
        for idx, piece in enumerate(pieces):
            if idx == 0 or idx == len(pieces) - 1:
                cells.append(piece)
                continue
            stripped = piece.strip()
            cells.append(f" {translate_inline(stripped)} " if stripped else " ")
        translated.append("|".join(cells))
    return translated


def parse_frontmatter(lines):
    if not lines or lines[0].strip() != "---":
        return None, lines
    for idx in range(1, len(lines)):
        if lines[idx].strip() == "---":
            return lines[: idx + 1], lines[idx + 1 :]
    return None, lines


def translate_frontmatter(lines):
    translated = []
    for line in lines:
        if line.startswith("sidebar_label:"):
            _, value = line.split(":", 1)
            value = value.strip().strip('"')
            translated_value = TITLE_OVERRIDES.get(value, translate_plain_text(value))
            translated.append(f'sidebar_label: "{translated_value}"')
        else:
            translated.append(line)
    return translated


def is_table_start(lines, index):
    if index + 1 >= len(lines):
        return False
    return lines[index].lstrip().startswith("|") and re.match(r"^\|(?:\s*[-: ]+\|)+\s*$", lines[index + 1].strip()) is not None


def translate_lines(body_lines):
    output = []
    i = 0
    while i < len(body_lines):
        line = body_lines[i]
        stripped = line.strip()

        if not stripped:
            output.append("")
            i += 1
            continue

        if stripped.startswith("<!--") or re.match(r"^<a\s+id=", stripped):
            output.append(line)
            i += 1
            continue

        if stripped.startswith("```"):
            fence = [line]
            i += 1
            while i < len(body_lines):
                fence.append(body_lines[i])
                if body_lines[i].strip().startswith("```"):
                    i += 1
                    break
                i += 1
            output.extend(fence)
            continue

        if re.match(r"^#{1,6}\s", stripped):
            output.append(translate_heading(line))
            i += 1
            continue

        if is_table_start(body_lines, i):
            table_lines = [body_lines[i], body_lines[i + 1]]
            i += 2
            while i < len(body_lines) and body_lines[i].lstrip().startswith("|"):
                table_lines.append(body_lines[i])
                i += 1
            output.extend(translate_table(table_lines))
            continue

        if re.match(r"^\s*>\s?", line):
            block = [line]
            i += 1
            while i < len(body_lines) and body_lines[i].strip().startswith(">"):
                block.append(body_lines[i])
                i += 1
            output.append(translate_blockquote("\n".join(block)))
            continue

        if re.match(r"^\s*(?:[-*]|\d+\.)\s+", line):
            block = [line]
            i += 1
            while i < len(body_lines):
                next_line = body_lines[i]
                if not next_line.strip():
                    break
                if re.match(r"^\s*(?:[-*]|\d+\.)\s+", next_line):
                    break
                if re.match(r"^#{1,6}\s", next_line.strip()) or next_line.strip().startswith("```"):
                    break
                if next_line.strip().startswith(">") or re.match(r"^<a\s+id=", next_line.strip()):
                    break
                block.append(next_line)
                i += 1
            output.append(translate_list_item("\n".join(block)))
            continue

        block = [line]
        i += 1
        while i < len(body_lines):
            next_line = body_lines[i]
            next_stripped = next_line.strip()
            if not next_stripped:
                break
            if next_stripped.startswith("```") or next_stripped.startswith("<!--"):
                break
            if re.match(r"^#{1,6}\s", next_stripped):
                break
            if re.match(r"^\s*(?:[-*]|\d+\.)\s+", next_line):
                break
            if next_stripped.startswith(">") or re.match(r"^<a\s+id=", next_stripped):
                break
            block.append(next_line)
            i += 1
        output.append(translate_paragraph("\n".join(block)))

    return output


def translate_file(source_path, force=False):
    rel = source_path.relative_to(ROOT)
    target = ZH_ROOT / rel
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists() and not force:
        return False

    lines = source_path.read_text(encoding="utf-8").splitlines()
    frontmatter, body_lines = parse_frontmatter(lines)

    output = []
    if frontmatter:
        output.extend(translate_frontmatter(frontmatter))
        output.append("")

    output.extend(translate_lines(body_lines))
    translated_text = "\n".join(output).rstrip() + "\n"
    source_text = source_path.read_text(encoding="utf-8")
    translated_text = normalize_link_targets(source_text, translated_text)
    target.write_text(translated_text, encoding="utf-8")
    return True


def repair_file(source_path):
    rel = source_path.relative_to(ROOT)
    target = ZH_ROOT / rel
    if not target.exists():
        return False
    source_text = source_path.read_text(encoding="utf-8")
    translated_text = target.read_text(encoding="utf-8")
    repaired_text = normalize_link_targets(source_text, translated_text)
    if repaired_text != translated_text:
        target.write_text(repaired_text, encoding="utf-8")
        return True
    return False


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("files", nargs="*")
    parser.add_argument("--repair-links-only", action="store_true")
    args = parser.parse_args()

    ZH_ROOT.mkdir(exist_ok=True)
    if args.files:
        files = [ROOT / item for item in args.files]
    else:
        files = list(english_docs())
    completed = 0
    for index, path in enumerate(files, start=1):
        if args.repair_links_only:
            wrote = repair_file(path)
        else:
            wrote = translate_file(path, force=bool(args.files))
        completed += 1 if wrote else 0
        print(f"[{index}/{len(files)}] {path.relative_to(ROOT)}", flush=True)
    print(json.dumps({"translated_files": completed, "target_root": str(ZH_ROOT.relative_to(ROOT))}, ensure_ascii=False))


if __name__ == "__main__":
    main()
