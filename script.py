<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Python Web App</title>
</head>
<body>
    <h1>Python Output</h1>
    <div id="output"></div>
    <script>
        fetch('https://api.github.com/repos/USERNAME/REPOSITORY_NAME/contents/path/to/python_output.txt')
        .then(response => response.json())
        .then(data => {
            document.getElementById('output').textContent = atob(data.content);
        });
    </script>
</body>
</html>
