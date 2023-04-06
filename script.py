import os

topics_files = os.listdir('topics')
readme = open('readme.md','r+')
readme_lines = readme.readlines()
readme_lines_lower = list(map(lambda x: x.lower(), readme_lines))
lines = len(readme_lines)
for topic_file in topics_files:
    topic = topic_file.split('.')[0] 
    if not any(topic in s for s in readme_lines_lower):
        to_write = "## {}. [{}]({}/{})\n".format(lines - 1, topic.capitalize(), 'topics', topic_file)
        readme.write(to_write)
        lines += 1

readme.close()

