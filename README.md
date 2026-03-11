# AI Platform Starter

这是一个用于快速启动 **AI 平台后端** 的最小可运行模板，包含：

- FastAPI 服务骨架
- 统一的模型提供方接口（可扩展 OpenAI / Azure / 本地模型）
- 基础聊天接口 `/v1/chat/completions`
- 健康检查 `/health`
- 自动化测试（pytest）

## 快速开始

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
uvicorn app.main:app --reload --port 8000
```

## 调用示例

```bash
curl -X POST http://127.0.0.1:8000/v1/chat/completions \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "mock-gpt",
    "messages": [
      {"role": "user", "content": "你好，介绍一下这个平台"}
    ]
  }'
```

## 目录结构

```text
app/
  main.py        # API 入口
  schemas.py     # 请求/响应结构
  services.py    # Provider 抽象与 Mock 实现
tests/
  test_api.py    # 接口测试
```
