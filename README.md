[![MseeP.ai Security Assessment Badge](https://mseep.net/pr/jonafly-rednotemcp-badge.png)](https://mseep.ai/app/jonafly-rednotemcp)

小红书自动评论工具（MCP Server）
这是一款基于 Playwright 开发的小红书自动搜索和评论工具，作为 MCP Server，可通过特定配置接入 MCP Client，帮助用户自动完成登录小红书、搜索关键词、获取笔记内容及发布智能评论等操作。

一、功能特点
自动登录：支持手动扫码登录方式，首次登录成功后会保存登录状态，后续使用无需重复扫码。
关键词搜索：能依据用户输入的关键词搜索小红书笔记，并可指定返回结果的数量。
笔记内容获取：输入笔记的 URL，即可获取该笔记的详细内容。
笔记评论获取：通过笔记 URL 获取相应笔记的评论信息。
智能评论发布：支持多种评论类型，包括引流（引导用户关注或私聊）、点赞（简单互动获取好感）、咨询（以问题形式增加互动）、专业（展示专业知识建立权威），可根据需求选择发布。

二、安装步骤
Python 环境检查：确保系统已安装 Python 3.8 或更高版本。若未安装，可从 Python 官方网站下载并安装。
项目获取：将本项目克隆或下载到本地。

安装依赖：在项目目录下打开命令行，执行以下命令安装所需依赖：
pip install -r requirements.txt

浏览器安装：首次运行工具时，会自动安装所需的浏览器。

三、MCP Server 配置
在 MCP Client 的配置文件中添加以下内容，将本工具配置为 MCP Server：
json
{
    "mcpServers": {
        "xiaohongshu MCP": {
            "command": "python",
            "args": [
                "/ABSOLUTE/PATH/TO/PARENT/FOLDER/xiaohongshu_mcp.py",
                "--stdio"
            ]
        }
    }
}
请根据实际情况调整args中的文件路径。

四、使用方法
（一）启动工具
若通过 MCP Client 启动，按照 MCP Client 的操作流程进行启动。

若直接运行，在项目目录下的命令行中执行：
bash
python main.py
（二）主要功能操作
登录小红书：启动工具后，若尚未登录，会打开浏览器窗口，等待用户手动扫码登录。登录成功后，工具会保存登录状态。
搜索笔记：在代码中调用search_notes函数，示例如下：
python
# 搜索美食相关的笔记，返回前3条结果
await search_notes("美食", 3)
获取笔记内容：使用get_note_content函数获取指定 URL 的笔记内容，示例如下：
python
# 获取指定URL的笔记内容
await get_note_content("https://www.xiaohongshu.com/search_result/xxxx")
获取笔记评论：调用get_note_comments函数获取指定 URL 笔记的评论，示例如下：
python
# 获取指定URL的笔记评论
await get_note_comments("https://www.xiaohongshu.com/search_result/xxxx")
发布智能评论：利用post_smart_comment函数在指定笔记发布评论，可选择不同的评论类型，示例如下：
python
# 在指定笔记发布咨询类型的评论
await post_smart_comment("https://www.xiaohongshu.com/search_result/xxxx", "咨询")
评论类型参数可选值：
"引流"（默认）：引导用户关注或私聊
"点赞"：简单互动获取好感
"咨询"：以问题形式增加互动
"专业"：展示专业知识建立权威
五、代码结构
docs/xiaohongshu_mcp.py：实现主要功能的核心文件，包含登录、搜索、获取内容和评论、发布评论等功能的代码逻辑。
main.py：示例调用脚本，用于展示如何调用xiaohongshu_mcp.py中的功能。
requirements.txt：记录项目所需的依赖库，通过pip install -r requirements.txt命令安装这些依赖。

六、注意事项
浏览器模式：工具使用 Playwright 的非隐藏模式运行，运行时会打开真实浏览器窗口。
登录方式：首次登录需要手动扫码，后续使用若登录状态有效，则无需再次扫码。
平台规则：使用过程中请严格遵守小红书平台的相关规定，避免进行过度操作，防止账号面临封禁等风险。
功能兼容性：由于小红书平台可能会进行更新和调整，搜索结果和评论功能的可用性可能会受到影响。若出现异常，请及时关注项目更新或联系开发者。

七、免责声明
本工具仅用于学习和研究目的，使用者应严格遵守相关法律法规以及小红书平台的规定。因使用不当导致的任何问题，本项目开发者不承担任何责任。