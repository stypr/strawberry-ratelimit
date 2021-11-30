## Strawberry GraphQL Ratelimit Extension

### Installation

```
pip3 install strawberry-ratelimit
```

### Usage

```py
my_schema = strawberry.Schema(
    query=Query,
    mutation=Mutation,
    extensions=[
        # 100 req / 1min
        ExtensionRatelimit(
            type_name=['getMusicByLevel'],
            rate_max=60,
            rate_seconds=60,
            depth_max=50, # Maximum depth of the query
            call_max=500 # Maximum call count
        )
    ]
)
```

### Limitations
