# Telegram 历史消息文件 (json) 分割

修改 group_title, group_type, group_id, 这三项应该与导出的文件中的 `name`, `type`, `id` 一致,

**group_id 不要带 -100 前缀**

把 `result.json` 放在脚本同目录下, 安装 `ijson` 和 `loguru` 后运行

```bash
python main.py
```