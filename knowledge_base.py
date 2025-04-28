import json

class KnowledgeBase:
    def __init__(self):
        # 初始化一个空的知识库，存储航海术语及其定义
        self.kb = {}

    def add_term(self, term, definition):
        """添加一个新的术语到知识库"""
        self.kb[term] = definition
        print(f"Term '{term}' added successfully!")

    def get_definition(self, term):
        """查询术语定义"""
        return self.kb.get(term, "该术语未在知识库中找到。")

    def list_terms(self):
        """列出所有术语"""
        return list(self.kb.keys())

    def save_to_file(self, filename):
        """将知识库保存到文件"""
        with open(filename, 'w') as file:
            json.dump(self.kb, file, ensure_ascii=False, indent=4)
        print(f"知识库已保存至文件: {filename}")

    def load_from_file(self, filename):
        """从文件加载知识库"""
        try:
            with open(filename, 'r') as file:
                self.kb = json.load(file)
            print(f"知识库已从文件 '{filename}' 加载。")
        except FileNotFoundError:
            print(f"文件 '{filename}' 未找到！")