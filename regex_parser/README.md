# A basic regex parser

```
input: text = "aa", pattern = "a"
false
```

```
input: text = "aa", pattern = "aa"
true
```

```
input: text = "aa", pattern = "a.c"
true
```

```
input: text = "abbb", pattern = "ab*"
true
```

```
input: text = "acd", pattern = "ab*c"
true
```