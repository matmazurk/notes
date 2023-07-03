# Golang

## Capture SIGINT

Package signal will not block sending to c: the caller must ensure that c has sufficient buffer space to keep up with the expected signal rate. For a channel used for notification of just one signal value, a buffer of size 1 is sufficient.

```go
c := make(chan os.Signal, 1)
signal.Notify(c, os.Interrupt)
...
<-c
```


## JSON struct tags

```go
// Field appears in JSON as key "myName".
Field int `json:"myName"`

// Field appears in JSON as key "myName" and
// the field is omitted from the object if its value is empty,
// as defined above.
Field int `json:"myName,omitempty"`

// Field appears in JSON as key "Field" (the default), but
// the field is skipped if empty.
// Note the leading comma.
Field int `json:",omitempty"`

// Field is ignored by this package.
Field int `json:"-"`

// Field appears in JSON as key "-".
Field int `json:"-,"`
```

## Slice header
```go
sh := (*reflect.SliceHeader)(unsafe.Pointer(&newSlice2))
```

### Without reflection
```go
//address of underlying array
s := []int{1,2,3}
fmt.Printf("addr:%p", &s[0])
```