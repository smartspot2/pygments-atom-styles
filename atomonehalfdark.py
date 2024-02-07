"""
A custom Pygments style for Atom One Half Dark.

Original syntax highlighting from:
https://github.com/sonph/onehalf
"""

from pygments.style import Style
from pygments.token import Text, Keyword, Name, Comment, Punctuation, String, Error, Literal, Number, Operator, Generic

BLACK = '#282C34'
RED = '#E06C75'
GREEN = '#98C379'
YELLOW = '#E5C07B'
BLUE = '#61AFEF'
PURPLE = '#C678DD'
CYAN = '#56B6C2'
WHITE = '#DCDFE4'

FG = WHITE
BG = BLACK

COMMENT_FG = '#5C6370'
GUTTER_BG = '#282C34'
GUTTER_FG = '#919BAA'
NON_TEXT = '#373C45'

class AtomOneHalfDarkStyle(Style):
    background_color = BG
    default_style = FG

    styles = {
        Text: FG,

        Keyword: RED,
        Keyword.Constant: CYAN,
        # Keyword.Declaration: None,
        Keyword.Namespace: CYAN,
        # Keyword.Pseudo: None,
        # Keyword.Reserved: None,
        Keyword.Type: YELLOW,

        Name: RED,
        Name.Attribute: YELLOW,
        Name.Builtin: BLUE,
        Name.Builtin.Pseudo: YELLOW,
        Name.Class: YELLOW,
        Name.Constant: YELLOW,
        Name.Decorator: BLUE,
        # Name.Entity: None,
        Name.Exception: BLUE,
        Name.Function: BLUE,
        Name.Function.Magic: CYAN,
        Name.Label: PURPLE,
        # Name.Namespace: None,
        # Name.Other: None,
        Name.Tag: RED,
        Name.Variable: RED,

        Literal: YELLOW,
        String: GREEN,
        # String.Affix: None,
        # String.Backtick: None,
        # String.Char: None,
        # String.Delimiter: None,
        # String.Doc: None,
        # String.Double: None,
        String.Escape: CYAN,
        # String.Heredoc: None,
        # String.Interpol: None,
        # String.Other: None,
        # String.Regex: None,
        # String.Single: None,
        # String.Symbol: None,

        Number: YELLOW,
        # Number.Bin: None,
        # Number.Float: None,
        # Number.Hex: None,
        # Number.Integer: None,
        # Number.Integer.Long: None,
        # Number.Oct: None,

        Operator: FG,
        Operator.Word: PURPLE,

        Punctuation: FG,

        Comment: f'italic {COMMENT_FG}',
        # Comment.Hashbang: None,
        # Comment.Multiline: None,
        # Comment.Preproc: None,
        # Comment.Single: None,
        Comment.Special: PURPLE,

        Generic: FG,
        Generic.Deleted: COMMENT_FG,
        Generic.Emph: f'italic {FG}',
        Generic.Error: RED,
        Generic.Heading: f'bold {FG}',
        # Generic.Inserted: None,
        # Generic.Output: None,
        # Generic.Prompt: None,
        Generic.Strong: f'bold {FG}',
        # Generic.Subheading: None,
        Generic.Traceback: f'italic {YELLOW}',
    }

