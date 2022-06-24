{
    description = "Nix Development Environment";

    inputs = {
        nixpkgs.url = "github:NixOS/nixpkgs/22.05";
        flake-utils.url = "github:numtide/flake-utils";
        devshell.url = "github:numtide/devshell";
    };

    outputs = { self,
        nixpkgs,
        flake-utils,
        devshell,
    }:
        flake-utils.lib.eachDefaultSystem (system: {
            devShells.default = 
                let pkgs = import nixpkgs {
                    inherit system;
                    overlays = [ devshell.overlay ];
                };
                in pkgs.devshell.mkShell {
                    imports = [ (pkgs.devshell.importTOML ./devshell.toml) ];
                };
        });
}
