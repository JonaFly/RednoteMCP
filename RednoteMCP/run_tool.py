import argparse
import asyncio
from fastmcp import Client
from xiaohongshu_mcp import mcp

async def main():
    parser = argparse.ArgumentParser(description="Run MCP tools via command line")
    parser.add_argument("tool", type=str, help="Name of the tool to call (e.g. login, search_notes)")
    parser.add_argument("--keywords", type=str, help="Keywords for search_notes")
    parser.add_argument("--limit", type=int, help="Limit for search_notes")
    parser.add_argument("--url", type=str, help="Note URL for get_note_content / get_note_comments / post_smart_comment")
    parser.add_argument("--comment_type", type=str, help="Comment type for post_smart_comment")
    args = parser.parse_args()

    async with Client(mcp) as client:
        params = {}
        if args.keywords: params["keywords"] = args.keywords
        if args.limit: params["limit"] = args.limit
        if args.url: params["url"] = args.url
        if args.comment_type: params["comment_type"] = args.comment_type

        print(f"\n🚀 调用工具: {args.tool}")
        print(f"🧾 参数: {params}\n")

        try:
            result = await client.call_tool(args.tool, params)
            print("✅ 返回结果：\n")
            print(result)
        except Exception as e:
            print(f"❌ 调用失败: {e}")

if __name__ == "__main__":
    asyncio.run(main())
