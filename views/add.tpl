<!-- タスク追加の画面のhtml -->

<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <title>ToDo App - 新しいタスク追加</title>
    <link rel="stylesheet" type="text/css" href="/static/style.css">
</head>
<body>
    <form method="post" action="/add_task", accept-charset="UTF-8">
        <label for="title">タイトル:</label>
        <input type="text" id="title" name="title" required>
        <br>
        <label for="description">詳細:</label>
        <textarea id="description" name="description"></textarea>
        <br>
        <button type="submit">タスクを追加</button>
    </form>
    <br>
    <h2><a href="/">未完了タスク一覧へ</a></h2>
    <h2><a href="/completed">完了タスク一覧へ</a></h2>
</body>
</html>
