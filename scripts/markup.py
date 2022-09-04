line_count = 1
speaker_count = 0

with open("test.txt", "r", encoding="utf-8") as f:
    text = f.readlines()

new_lines = []

for line in text:
    new_line = f"10.{line_count:03d}.{speaker_count:02d} {line}"
    if speaker_count == 1:
        line_count = line_count + 1
    if speaker_count == 0:
        speaker_count = 1
    elif speaker_count == 1:
        speaker_count = 0
    new_lines.append(new_line)

with open("test_out.txt", "w", encoding="utf-8") as g:
    g.writelines(new_lines)