Demo ZK
-------

*Warning* : This is a demo project, it is not intended to be used in production.

This project is a demo of a ZK application. It is a simple application that allows you to verify the validity of a proof generated using the groth16 scheme. 


## Use 

### Node Setup

1. Clone the [Sandbox][sandbox] repo
2. Copy `sandbox/config.zk` into the sandbox repo root
3. Copy `sandbox/DevModeNetwork.json` into the sandbox repo at `images/algod/DevModeNetwork.json` 
4. In the sandbox repo, run `./sandbox up zk`
5. Wait for the sandbox to start up

### Demo Setup

Install [Zokrates][zokrates] using the instructions [here][zokrates-install].

Run the generate script to generate the proof.

```bash
./generate_proof.sh
```

Optionally modify the current `.zok` file to generate a different proof.

*Note* This must be done prior to running the contract since it relies on the Verification Key and Proof generated during this step

### Demo

Install python prereqs

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

[zokrates]: https://zokrates.github.io/
[zokrates-install]: https://zokrates.github.io/gettingstarted.html#one-line-installation
[sandbox]: htts://github.com/algorand/sandbox
