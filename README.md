Demo ZK
-------

:warning: This is a demo project, it is not intended to be used in production. :warning: 

This project is a demo of a simple ZK application that allows verifying a proof generated using the groth16 scheme and the BLS12_381 curve. 

This demo only shows the verification of a proof using BLS12_381 but BN254 is also supported in the AVM. However, Zokrates does not support [BN254 curve][zokrates-curves], so a different library will be needed to generate a proof for that curve.  

## Use 

First clone this repo down

**Note**: This demo requires Python >= 3.10 

### Node Setup

In the `sandbox` directory, run `./setup.sh` to 

1. clone down the sandbox 
2. setup configuration, so it may run with the EC math ops
3. start the sandbox node

### Demo Setup

Install [Zokrates][zokrates] using the instructions [here][zokrates-install].

Run the `generate_proof` script to generate the Verification Key and Proof

```bash
./generate_proof.sh
```

**Note:** This must be done prior to running the contract since it relies on the Verification Key and Proof generated during this step

### Demo

Install python prerequisites

```bash
$ python -m venv .venv
$ source .venv/bin/activate
(.venv) $ pip install -r requirements.txt
```

Run the demo

```bash
(.venv) $ cd contracts 
(.venv) $ python main.py
```

You should see some output like 
```bash
(.venv) $ python main.py
Created app: 1
Contract verified? True
```

## Going Further

Modify the `.zok` file to change the proof that is generated to something more interesting.

Generate a proof using a different library to use the `BN254` curve


[zokrates]: https://zokrates.github.io/
[zokrates-install]: https://zokrates.github.io/gettingstarted.html#one-line-installation
[zokrates-curves]: https://zokrates.github.io/toolbox/proving_schemes.html#curves
[sandbox]: https://github.com/algorand/sandbox
