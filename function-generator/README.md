## Code injection process

1. Docker build with CODE env which contain user code

2. When docker run, CODE env is injected from Custom Resource of k8s

3. Docker running cmd example
```bat
docker run -p 8080:80 -e CODE="@app.post('/test')\nasync def test_func(req:Request):\n\treturn await req.body()" python-serverless-test
```

