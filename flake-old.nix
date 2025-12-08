{
  inputs = {
    nixpkgs = {
      url = "github:nixos/nixpkgs/nixos-unstable";
    };
    flake-utils = {
      url = "github:numtide/flake-utils";
    };
    jupyterWith = {
      url = "github:tweag/jupyterWith";
      flake = false;
    };
  };
  outputs = { nixpkgs, flake-utils, jupyterWith, ... }: flake-utils.lib.eachDefaultSystem (system:
    let
      jupyter = import jupyterWith {};
      pkgs = import nixpkgs {
        inherit system;
      };
      iPython = jupyter.kernels.iPythonWith {
        name = "python";
        packages = p: with p; [ numpy ];
      };

      jupyterEnvironment =
        jupyter.jupyterlabWith {
          kernels = [ iPython ];
        };
    in
    rec {
      # devShell = jupyterEnvironment.env;
      devShell = pkgs.mkShell {
        buildInputs = with pkgs; [
          (python39.withPackages(ps: with ps; [
            ipython
            jupyterlab
            numpy
            pandas
            nix-kernel
            scipy
            ply
          ]))
          ghc
          gdb
        ];
        shellHook = "jupyter-lab";
      };
    }
  );
}
