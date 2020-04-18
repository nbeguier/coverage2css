# Coverage 2 CSS

[![Python 3.4|3.8](https://img.shields.io/badge/python-3.4|3.8-green.svg)](https://www.python.org/) [![License](https://img.shields.io/github/license/nbeguier/coverage2css?color=blue)](https://github.com/nbeguier/coverage2css/blob/master/LICENSE)

Uses the Chrome Coverage to extract used CSS from original CSS

## Prerequisites

  - Export the Chrome report of a css file: https://developers.google.com/web/tools/chrome-devtools/coverage
  - Download the css file

## Usage

```
$ ./coverage2css.py <json coverage> <css file>
```

## Example

```
$ ./coverage2css.py Coverage-20200418T105522.json bootstrap.min.css
> Detect 'common.js' in report
> Detect 'embeds.js' in report
> Detect 'page_performance.js' in report
> Detect '' in report
> Detect 'home-style.min.css' in report
> Detect 'bootstrap.min.css' in report
>> Match input file
>> Write bootstrap.min.css.new
> Detect 'ionicons.css' in report
> Detect 'redirect.min.js' in report
> Detect 'css?family=Playfair+Display:700,900' in report
```

# License
Licensed under the [MIT License](https://github.com/nbeguier/coverage2css/blob/master/LICENSE).

# Copyright
Copyright 2020 Nicolas Béguier; ([nbeguier](https://beguier.eu/nicolas/) - nicolas_beguier[at]hotmail[dot]com)
