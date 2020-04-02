from gym.envs.registration import register

register(
    id='my_env-v0',
    entry_point='my_env.envs:FooEnv',
)
register(
    id='my_env-extrahard-v0',
    entry_point='my_env.envs:FooExtraHardEnv',
)