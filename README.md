# 修改：
相较于main版本修改了一点，解决了issue中提到的错误
按照原版本操作即可，也可以看以下完整版：

## 注意先进入RednoteMCP文件夹
## 安装依赖
pip install -r requirements.txt
下载playwright
playwright install
## 登录
python run_tool.py login
## 其他功能
### 搜索笔记内容 美妆可以被其他你想要在搜索框中输入的内容代替
python run_tool.py search_notes --keywords 美妆 --limit 2
### 获取笔记正文内容 你可以从 search_notes 的结果中拷贝 URL 使用
python run_tool.py get_note_content --url “https://www.xiaohongshu.com/explore/xxxxx”

### 发布智能评论（四种类型）
 **--comment_type** 可选值如下：
-  引流：引导用户关注或私聊
-  点赞：表达赞同，增强互动
-  咨询：提出问题，引导对话- # 专业：展示知识，建立权威
  比如
python run_tool.py post_smart_comment --url “https://www.xiaohongshu.com/xxxxx” --comment_type 咨询

