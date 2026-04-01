# cli.py

import argparse
from sync.sync_runner import run_sync

def main():
    parser = argparse.ArgumentParser(description="Sync Obsidian notes to Confluence")
    parser.add_argument("--config", type=str, default="config/default.yaml", help="Path to config.yaml")
    parser.add_argument("--state", type=str, default="sync_state.json", help="Path to sync state file")
    parser.add_argument("--tag", type=str, help="Override tag filter")
    parser.add_argument("--dir", type=str, nargs="*", help="Override include_dirs list")
    parser.add_argument("--dry-run", action="store_true", help="Only print actions without uploading")

    args = parser.parse_args()

    run_sync(
        config_path=args.config,
        state_path=args.state,
        tag_override=args.tag,
        dirs_override=args.dir,
        dry_run=args.dry_run
    )

if __name__ == "__main__":
    main()