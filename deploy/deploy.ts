import { Wallet } from "zksync-web3";
import { HardhatRuntimeEnvironment } from "hardhat/types";
import { Deployer } from "@matterlabs/hardhat-zksync-deploy";
import "dotenv/config";

export default async function (hre: HardhatRuntimeEnvironment) {
  console.log("Deploying Disperse contract to zkSync...");
  const mnemonic: string | undefined = process.env.MNEMONIC;
  if (!mnemonic) throw new Error("Mnemonic not found in .env file");
  const wallet = Wallet.fromMnemonic(mnemonic);

  const deployer = new Deployer(hre, wallet);
  const artifact = await deployer.loadArtifact("Disperse");

  const disperseContract = await deployer.deploy(artifact);
  console.log("Disperse deployed to: ", disperseContract.address);
}
