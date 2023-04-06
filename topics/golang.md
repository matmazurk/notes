# Golang

## Capture SIGINT

Package signal will not block sending to c: the caller must ensure that c has sufficient buffer space to keep up with the expected signal rate. For a channel used for notification of just one signal value, a buffer of size 1 is sufficient.

```go
c := make(chan os.Signal, 1)
signal.Notify(c, os.Interrupt)
...
<-c
```