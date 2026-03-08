"""Rich ライブラリを使った複数行プログレスバーのデモ。

複数のタスクが並行して進行する様子をターミナル上で表示する。
"""

import time
import random

from rich.console import Console
from rich.progress import (
    Progress,
    BarColumn,
    SpinnerColumn,
    TextColumn,
    TimeElapsedColumn,
    TimeRemainingColumn,
    TaskProgressColumn,
)

console = Console()


def simulate_tasks() -> None:
    """複数タスクの並行プログレスをシミュレートする。"""

    progress = Progress(
        SpinnerColumn(),
        TextColumn("[bold blue]{task.description}"),
        BarColumn(bar_width=40),
        TaskProgressColumn(),
        TimeElapsedColumn(),
        TimeRemainingColumn(),
        console=console,
    )

    tasks_config = [
        ("データダウンロード", 100),
        ("画像処理", 80),
        ("モデル学習", 60),
        ("レポート生成", 40),
        ("ログ圧縮", 120),
    ]

    with progress:
        task_ids = []
        for description, total in tasks_config:
            task_id = progress.add_task(description, total=total)
            task_ids.append(task_id)

        # 全タスクが完了するまでループ
        while not all(
            progress.tasks[tid].completed >= progress.tasks[tid].total
            for tid in task_ids
        ):
            for tid in task_ids:
                task = progress.tasks[tid]
                if task.completed < task.total:
                    advance = random.uniform(0.5, 3.0)
                    progress.advance(tid, advance)
            time.sleep(0.05)


if __name__ == "__main__":
    console.print("[bold green]>>> 複数行プログレスバーのデモ開始[/bold green]\n")
    simulate_tasks()
    console.print("\n[bold green]>>> 全タスク完了！[/bold green]")
