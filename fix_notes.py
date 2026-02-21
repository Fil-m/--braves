import re

def process_file():
    with open('discover.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract the NOTES dictionary block
    notes_match = re.search(r'const NOTES = \{([\s\S]*?)\};\s*Object\.entries\(NOTES\)\.forEach\(\(\[name, note\]\) => \{[\s\S]*?\}\);', content)
    if not notes_match:
        print("Could not find the NOTES block.")
        return

    notes_block = notes_match.group(1)
    
    # Parse individual notes into a dictionary
    notes = {}
    for line in notes_block.split('\n'):
        # match patterns like: q1: 'text',
        m = re.search(r'(q\d+):\s*\'([^\']+)\'', line)
        if m:
            notes[m.group(1)] = m.group(2)

    # For each note, find the corresponding tr and inject the note statically into q-text
    new_content = content
    for q_id, note_text in notes.items():
        # Find the <td class="q-text">...</td> inside <tr data-q="X">
        # Pattern looks for <tr data-q="X"> then finds <td class="q-text">...</td>
        # We need to append the span.q-note to the contents of that td
        
        # Build a regex to find the closing td tag specifically for the right question
        q_num = q_id.replace('q', '')
        pattern = r'(<tr data-q="{}">[\s\S]*?<td class="q-text">[\s\S]*?)(</td>)'.format(q_num)
        
        # Replace function to append the span before the closing td
        def replacer(match):
            return match.group(1) + f'\n                    <span class="q-note">{note_text}</span>' + match.group(2)
            
        new_content = re.sub(pattern, replacer, new_content)

    # Remove the JS block from the file
    new_content = new_content.replace(notes_match.group(0), '// Removed dynamic NOTES injection.')

    with open('discover.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
        
    print("Injected notes statically and removed JS block.")

if __name__ == '__main__':
    process_file()
