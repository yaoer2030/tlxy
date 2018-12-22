# 以下为Python编程入门到实践7.2.2的源码
prompt = "\ntell me sonmething, and i will repeat it back to you:"
prompt += "\nenter 'quit' to end the prompt"
message = " "  # 如果这里不定义空值变量  while循环开始没有可对比的条件,会报错
while message != 'quit':
    message = input(prompt)
    print(message)



