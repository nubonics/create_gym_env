from gym.envs.registration import register

register(
    id='my_env-v0',
    entry_point='my_env.envs:MyEnvEnv',
)
register(
    id='my-extrahard-v0',
    entry_point='my_env.envs:MyExtraHardEnv',
)