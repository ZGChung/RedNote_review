SYSTEM_PROMPT = """你是一位经验丰富的专业文档审核员，具有广泛的技术写作和文档编制经验。
你的角色是对文档部分提供全面、建设性的反馈，同时保持专业和乐于助人的语气。"""

USER_PROMPT_SUGGESTION = """请根据以下标准，对以下文本进行审核：
1. 内容清晰度：评估内容的清晰性和可理解性。
2. 语法和风格：检查语法错误和写作风格的一致性。
3. 技术准确性：验证技术信息是否准确且解释清晰。
4. 结构完整性：评估思想的逻辑流动和组织。

请您根据以上标准，对以下文本进行审核，并给出您的建议。
您的建议应当尽量详细，必须覆盖上述每个要点。
除了给出您的建议，不要返回任何的额外内容。

以下是待审查的文本：{}
现在请提供您的建议："""

USER_PROMPT_BETTER_TEXT = """请根据以下标准，对以下文本进行审核：
1. 内容清晰度：评估内容的清晰性和可理解性。
2. 语法和风格：检查语法错误和写作风格的一致性。
3. 技术准确性：验证技术信息是否准确且解释清晰。
4. 结构完整性：评估思想的逻辑流动和组织。

请您根据以上标准，对以下文本进行审核，并给出修改后的文本。
除了给出修改后的文本，不要返回任何的额外内容。

以下是待审查的文本：{}
现在请提供您的修改后的文本："""
