Web3-gear
---------

Proxy `Powerplay <https://github.com/playmakerchain/powerplay>`_'s RESTful API to Eth JSON-RPC, to support Remix, 
Truffle and more (You should give priority to using PowerPlay's RESTful API).

Working with `Powerplay Builtins <https://github.com/playmakerchain/powerplay-builtins>`_ will make Web3-Gear more 
usable.

Quick Start
-----------

Installation
>>>>>>>>>>>>

On OS x
:::::::

* Python 3.6+ support

1. Install the system-dependecies::

    brew install openssl
    export CFLAGS="-I$(brew --prefix openssl)/include $CFLAGS"
    export LDFLAGS="-L$(brew --prefix openssl)/lib $LDFLAGS"

2. Installation of Web3-Gear and it's dependent Python packages via PyPI::

    pip3 install web3-gear

On Ubuntu
:::::::::

* Python 3.6+ support

1. Install the system-dependecies::

    sudo apt-get install build-essential libssl-dev python-dev

2. Installation of Web3-Gear and it's dependent Python packages via PyPI::

    pip3 install web3-gear

On Window
:::::::::

* Python 3.6 support

1. Install Visual C++ Build Tools.

2. Install `scrypt-py <https://pypi.org/project/scrypt/#files>`_ use the precompiled wheels.

3. Installation of Web3-Gear and it's dependent Python packages via PyPI::

    pip3 install web3-gear

Run
>>>

Installing through pip will make the ``web3-gear`` command available on your machine (`must run powerplay client first.`)::

    web3-gear

This will run web3-gear on ``127.0.0.1:2884``.

You can change its default behavior with the following parameters:

--host      rpc service host, eg: ``--host 127.0.0.1``
--port      rpc service port, eg: ``--port 2884``
--endpoint  powerplay restful service endpoint, eg: ``--endpoint http://127.0.0.1:2885``
--keystore  keystore file path, eg: ``--keystore /Users/(username)/keystore)``, default=powerplay stand-alone(solo) built-in accounts
--passcode  passcode of keystore, eg: ``--passcode xxxxxxxx``


Use Truffle
>>>>>>>>>>>

* Truffle 4.0.6+ support

Modify the configuration of truffle first(``truffle.js``):

.. code-block:: js

    module.exports = {
        networks: {
            development: {
                host: "localhost",
                port: 2845,
                network_id: "*" // Match any network id
            }
        }
    };

Then you can use truffle's command line tool.

There are some projects based on truffle, can use them for testing:

- `Crowdsale Contracts <https://github.com/playmakerchain/crowdsale-contracts>`_.
- `Token Distribution <https://github.com/libotony/token-distribution>`_.
- `Solidity Idiosyncrasies <https://github.com/miguelmota/solidity-idiosyncrasies>`_.
