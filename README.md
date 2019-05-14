Web3-gear
---------

Proxy [Powerplay's](https://github.com/playmakerchain/powerplay) RESTful API to Eth JSON-RPC, to support Remix, Truffle and more (You should give priority to using Powerplay's RESTful API).

Working with [Powerplay Builtins](https://github.com/playmakerchain/powerplay-builtins) will make Web3-Gear more usable.

Quick Start
-----------

Installation
>>>>>>>>>>>>

On OS x
-

* Python 3.6+ support

1. Install the system dependancies:

	brew install openssl
	export CFLAGS="-I$(brew --prefix openssl)/include $CFLAGS"
	export LDFLAGS="-L$(brew --prefix openssl)/lib $LDFLAGS"

2. Installation of Web3-Gear and it's dependent Python packages via PyPI

