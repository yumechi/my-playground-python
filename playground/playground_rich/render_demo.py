"""Rich ライブラリによる Markdown レンダリングと Syntax ハイライトのデモ。"""

from rich.console import Console
from rich.markdown import Markdown
from rich.syntax import Syntax
from rich.panel import Panel

console = Console()

# --- Markdown レンダリング ---

SAMPLE_MARKDOWN = """\
# Rich Markdown デモ

Rich を使うと、ターミナル上で **Markdown** を描画できます。

## 機能一覧

- **太字**、*イタリック*、`インラインコード` に対応
- リストやテーブルも表示可能
- 引用やコードブロックもサポート

> これは引用ブロックです。
> ターミナルでも見やすく表示されます。

## コード例

```python
def greet(name: str) -> str:
    return f"Hello, {name}!"
```

| ライブラリ | 用途          |
|-----------|--------------|
| Rich      | ターミナル装飾 |
| Textual   | TUI構築       |
| Click     | CLI構築       |
"""

console.print(Panel("[bold]Markdown レンダリング[/bold]", style="green"))
md = Markdown(SAMPLE_MARKDOWN)
console.print(md)

console.print()

# --- Syntax ハイライト ---

SAMPLE_CODE = '''\
from dataclasses import dataclass


@dataclass
class Task:
    """タスクを表すデータクラス。"""

    name: str
    priority: int = 0
    done: bool = False

    def complete(self) -> None:
        self.done = True
        print(f"✔ {self.name} を完了しました")


def main() -> None:
    tasks = [
        Task("設計書を書く", priority=2),
        Task("テストを追加", priority=1),
        Task("デプロイ", priority=3),
    ]

    for task in sorted(tasks, key=lambda t: t.priority, reverse=True):
        task.complete()


if __name__ == "__main__":
    main()
'''

SAMPLE_JS = '''\
import express from "express";

const app = express();

app.get("/api/tasks", async (req, res) => {
  const { status, limit = 10 } = req.query;

  try {
    const tasks = await db.tasks
      .find({ status: status ?? "active" })
      .limit(Number(limit))
      .toArray();

    res.json({ ok: true, data: tasks });
  } catch (err) {
    console.error("Failed to fetch tasks:", err);
    res.status(500).json({ ok: false, error: "Internal server error" });
  }
});

app.listen(3000, () => {
  console.log("Server running on http://localhost:3000");
});
'''

SAMPLE_GO = '''\
package main

import (
\t"fmt"
\t"sync"
)

type Task struct {
\tName     string
\tPriority int
\tDone     bool
}

func (t *Task) Complete() {
\tt.Done = true
\tfmt.Printf("✔ %s を完了しました\\n", t.Name)
}

func main() {
\ttasks := []Task{
\t\t{Name: "設計書を書く", Priority: 2},
\t\t{Name: "テストを追加", Priority: 1},
\t\t{Name: "デプロイ", Priority: 3},
\t}

\tvar wg sync.WaitGroup
\tfor i := range tasks {
\t\twg.Add(1)
\t\tgo func(t *Task) {
\t\t\tdefer wg.Done()
\t\t\tt.Complete()
\t\t}(&tasks[i])
\t}
\twg.Wait()
\tfmt.Println("全タスク完了")
}
'''

samples = [
    ("Python", SAMPLE_CODE, "python"),
    ("JavaScript", SAMPLE_JS, "javascript"),
    ("Go", SAMPLE_GO, "go"),
]

for label, code, lang in samples:
    console.print(Panel(f"[bold]Syntax ハイライト ({label})[/bold]", style="green"))
    syntax = Syntax(code, lang, theme="monokai", line_numbers=True)
    console.print(syntax)
    console.print()
