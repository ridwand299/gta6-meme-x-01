// Copy POST.json from the bot directory to the output directory.
// Node 22 stdlib only. MAKEFUN_BOT_DIR defaults to /bot,
// MAKEFUN_OUTPUT_DIR defaults to /output. Exit 1 on copy failure.
// The copy is byte-for-byte: the X post URL in POST.json is the entry's
// proof, so this file never rewrites or reformats it, it only moves it.
import { copyFileSync, mkdirSync } from "node:fs";
import { join } from "node:path";

const botDir = process.env.MAKEFUN_BOT_DIR ?? "/bot";
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
const src = join(botDir, "POST.json");
const dst = join(outDir, "POST.json");

try {
  mkdirSync(outDir, { recursive: true });
  copyFileSync(src, dst);
  console.log(`copied ${src} to ${dst}`);
} catch (err) {
  console.error(`failed to copy ${src} to ${dst}: ${err}`);
  process.exit(1);
}
