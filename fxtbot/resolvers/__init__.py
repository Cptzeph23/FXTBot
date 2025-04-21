# flake8: noqa: F401
# isort: off
from fxtbot.resolvers.iresolver import IResolver
from fxtbot.resolvers.exchange_resolver import ExchangeResolver

# isort: on
# Don't import HyperoptResolver to avoid loading the whole Optimize tree
# from fxtbot.resolvers.hyperopt_resolver import HyperOptResolver
from fxtbot.resolvers.pairlist_resolver import PairListResolver
from fxtbot.resolvers.protection_resolver import ProtectionResolver
from fxtbot.resolvers.strategy_resolver import StrategyResolver
