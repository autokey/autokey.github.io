# Documentation maintenance: periodic link review audits
Links and their contents sometimes change and either need to be updated or removed and some working links (especially **GitHub** wiki anchors) produce false positives during documentation builds due to changing raw HTML rendering limits.

False positives are typically bypassed by adding them directly to the **linkcheck_ignore** list in the `conf.py` file. However, that list uses **regex**, making it fiddly to maintain. This project added an **ignored_links** list that's easier to maintain since it accepts plain-text URLs. The two lists are mapped together, so, the **linkcheck_ignore** list will process any links in the **ignored_links** list.

The links can be maintained by periodically doing a manual inspection, doing a local build of the documentation, and using the **Sphinx** `linkcheck` tool to ensure that all documentation links remain active and are valid.

### Steps
Use these steps to manage new and existing links:
1. [Build the documentation locally](https://github.com/autokey/autokey.github.io/blob/master/guides/build-local.md) and check the output for warnings about links.
2. Audit the links in the [conf.py](https://github.com/autokey/autokey.github.io/blob/master/conf.py) file's **ignored_links** list:
   1. Temporarily remove the links from the list.
   2. Run the `make linkcheck` command in a terminal window and check the output for warnings.
   3. Return any links that received warnings back to the **ignored_links** list.
   4. Discard the remaining links that were set aside and now pass the test.
   5. Audit the links that are still in the list to verify that they're still relevant:
      1. Copy each URL.
      2. Paste it into your browser's address bar.
      3. Examine the contents of the page.
   6. If a link that's in the **ignored_links** list is removed from its corresponding `.rst` file, also remove it from the **ignored_links** list.
3. Audit the links in the `.rst` source files to verify that they're still valid by testing them:
   1. Run the `make linkcheck` command in a terminal window and check the output for warnings.
   2. Update any links that have changed.
   3. Discard any links that no longer exist, replacing them with new ones, if possible.
4. Audit the links in the `.rst` source files to verify that they're still relevant for users:
   1. Manually click on each link.
   2. Examine its contents in the page.
   3. If it's no longer relevant, either update it with a relevant link or remove the link from the `.rst` file.
5. Audit a new link:
   1. With a new link in place in an `.rst` file, [build the documentation locally](https://github.com/autokey/autokey.github.io/blob/master/guides/build-local.md) and check its output for a warning.
   2. If it generates a false-positive warning:
      1. Add the link to the [conf.py](https://github.com/autokey/autokey.github.io/blob/master/conf.py) file's **ignored_links** list.
      2. Run the `make linkcheck` command in a terminal window and check the output to make sure it's being ignored.

### Notes
* When adding or removing links to or from the **ignored_links** list in the `conf.py` file, keep the **Python** syntax for strings in lists intact by surrounding each link with single quotes and adding a trailing comma to the end of **each** one. For example:
  ```python
   'https://example-one.com',
   'https://example-two.com',
  ```
