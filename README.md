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
        # 60req/min
        ExtensionRatelimit(
            type_name=['getUser', 'updateUser', 'user_friends'], # queries, mutations, internal funcs.
            rate_max=60,
            rate_seconds=60,
            depth_max=50, # Maximum depth of the query
            call_max=500 # Maximum call count
        )
    ]
)
```

### Limitations

* Consider this project as a reference code. Do not use it for production.

  * Currently, the code uses a single global dict variable to store users' query/mutation accesses.
  * Although there is a code to flush the list of user's IP after a certain amount of logs, the code itself does not collect garbage and it may consume a lot of memory depending on the number of users.
  * It is recommended to re-write this code with DB support for optimization.
