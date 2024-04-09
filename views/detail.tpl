<!-- タスク詳細の画面のhtml -->

<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <title>ToDo App - タスク詳細</title>
    <link rel="stylesheet" type="text/css" href="/static/style.css">
</head>
<body>
    <h1>タスク詳細</h1>
    <h2>{{task[1]}}</h2>
    <p>{{task[2]}}</p>
    <form action="/edit/{{task[0]}}" method="post">
        <label for="title">タイトル:</label>
        <input type="text" name="title" value="{{task[1]}}" required>
        <br>
        <label for="description">詳細:</label>
        <textarea name="description">{{task[2]}}</textarea>
        <br>
        <input type="submit" value="編集">
    </form>
    <br>
    <form action="/toggle/{{task[0]}}" method="get">
        <input type="submit" value="完了／未完了切り替え">
    </form>
    <form action="/delete/{{task[0]}}" method="get">
        <input type="submit" value="削除">
    </form>
    <br>
    <h2><a href="/">未完了タスク一覧へ</a></h2>
    <h2><a href="/completed">完了タスク一覧へ</a></h2>
</body>
</html>
