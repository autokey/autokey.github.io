## Bump the GitHub Action versions
The [GitHub Action](https://github.com/autokey/autokey.github.io/actions) versions should be checked and updated regularly.
1. Check for updates:
   * Review the [pages.yml](https://github.com/autokey/autokey.github.io/blob/master/.github/workflows/pages.yml) file on the **master** branch and compare current versions against the latest releases:
     * [actions/checkout](https://github.com/marketplace/actions/checkout)
     * [actions/upload-pages-artifact](https://github.com/marketplace/actions/upload-github-pages-artifact)
     * [actions/deploy-pages](https://github.com/marketplace/actions/deploy-github-pages-site).
2. Apply available updates on GitHub:
   1. Fork the repository.
   2. Create a new branch named **update_actions** off of the **master** branch.
   3. Edit the actions:
      1. Open the [pages.yml](https://github.com/autokey/autokey.github.io/blob/master/.github/workflows/pages.yml) file in the GitHub editor. 
      2. Click the **Edit** button.
      3. Update the version numbers that have changed (e.g., change **@v3** to **@v4**).
      4. Commit the change.
   4. Update change log:
      1. Open the [CHANGELOG.md](https://github.com/autokey/autokey.github.io/blob/master/CHANGELOG.md) file in the GitHub editor.
      2. Click the **Edit** button.
      3. Document the version bumps.
      4. Commit the change.
3. Submit a pull request:
   1. Open a pull request against the **master** branch of the repository.
4. Post-merge cleanup:
   1. Once an administrator merges the pull request:
      1. Open the merged pull request.
      2. Click the **Delete branch** button to keep your fork tidy.
      3. Synchronize the **master** branch in your fork to incorporate the change.
