<!-- 未完了タスクの画面のhtml -->

<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <title>ToDo App - 未完了タスク一覧</title>
    <link rel="stylesheet" type="text/css" href="/static/style.css">
</head>
<body>
    <h1>未完了タスク一覧</h1>
    <ul>
        % for task in tasks:
            <li>
                <a href="/task/{{task[0]}}">{{task[1]}}</a>
                <form action="/toggle/{{task[0]}}" method="get">
                    <input type="submit" value="完了">
                </form>
                <form action="/delete/{{task[0]}}" method="get">
                    <input type="submit" value="削除">
                </form>
            </li>
        % end
    </ul>
    <h2><a href="/completed">完了タスク一覧へ</a></h2>
    <h2><a href="/add">新しいタスクを追加</a></h2>
</body>
</html>
