import os
import json
import re

POSTS_DIR = 'posts'
OUTPUT_FILE = 'posts.json'

def parse_front_matter(content):
    """简单的解析 YAML 头部"""
    metadata = {}
    # 匹配 --- 之间的内容
    match = re.search(r'^---\s+(.*?)\s+---', content, re.DOTALL)
    if match:
        yaml_text = match.group(1)
        for line in yaml_text.split('\n'):
            if ':' in line:
                key, value = line.split(':', 1)
                metadata[key.strip()] = value.strip()
    return metadata

def build_index():
    posts = []
    files = [f for f in os.listdir(POSTS_DIR) if f.endswith('.md')]
    
    # 按文件名排序 (通常文件名带日期，所以等于按日期倒序)
    files.sort(reverse=True)

    for filename in files:
        filepath = os.path.join(POSTS_DIR, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            meta = parse_front_matter(content)
            
            # 如果没有 meta，就跳过或者用默认值
            if not meta: continue
            
            posts.append({
                "title": meta.get('title', '无标题'),
                "date": meta.get('date', 'Unknown'),
                "summary": meta.get('summary', ''),
                "file": filename  # 重要：告诉前端去加载哪个文件
            })
    
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(posts, f, ensure_ascii=False, indent=2)
    
    print(f"索引构建完成！共 {len(posts)} 篇文章。已更新 posts.json")

if __name__ == '__main__':
    build_index()