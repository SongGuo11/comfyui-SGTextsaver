class SGTextSaver:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": ("STRING", {"multiline": True}),
                "file_path": ("STRING", {"default": "./output"}),
                "file_name": ("STRING", {"default": "output.txt"}),
                "mode": ("BOOLEAN", {"default": False, "label_on": "Append", "label_off": "Overwrite"}),
                "add_newline": ("BOOLEAN", {"default": True, "label_on": "Yes", "label_off": "No"})
            }
        }

    RETURN_TYPES = ("BOOLEAN",)
    FUNCTION = "save_text"
    CATEGORY = "SG_Text/IO"
    OUTPUT_NODE = True

    def save_text(self, text, file_path, file_name, mode, add_newline):
        # 处理换行
        if add_newline:
            text += "\n"
            
        # 处理模式
        write_mode = "a" if mode else "w"
        
        # 确保路径存在
        import os
        os.makedirs(file_path, exist_ok=True)
        
        # 保存文件
        full_path = os.path.join(file_path, file_name)
        with open(full_path, write_mode, encoding='utf-8') as f:
            f.write(text)
            
        return (True,)