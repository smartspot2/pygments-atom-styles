"""
A custom Pygments style for Atom One Dark.

Original syntax highlighting from:
https://github.com/atom/atom/blob/master/packages/one-dark-syntax/
"""

from pygments.style import Style
from pygments.token import Text, Keyword, Name, Comment, Punctuation, String, Error, Literal, Number, Operator, Generic

MONO1 = '#ABB2BF'  # hsl(220, 14%, 71%);
MONO2 = '#828997'  # hsl(220, 9%, 55%);
MONO3 = '#5C6370'  # hsl(220, 10%, 40%);

HUE1 = '#56B6C2'  # hsl(187, 47%, 55%); cyan
HUE2 = '#61AFEF'  # hsl(207, 82%, 66%); blue
HUE3 = '#C678DD'  # hsl(286, 60%, 67%); purple
HUE4 = '#98C379'  # hsl( 95, 38%, 62%); green
HUE5 = '#E06C75'  # hsl(355, 65%, 65%); red 1
HUE52 = '#BE5046'  # hsl(  5, 48%, 51%); red 2
HUE6 = '#D19a66'  # hsl( 29, 54%, 61%); orange 1
HUE62 = '#E5C07B'  # hsl( 39, 67%, 69%);

FG = MONO1
BG = '#282C34'  # hsl(220, 13%, 18%);

GUTTER = '#636D83'  # hsl(220, 14%, 45%);
ACCENT = '#528BFF'  # hsl(220, 100%, 66%);


class AtomOneDarkStyle(Style):
    background_color = BG
    default_style = FG

    styles = {
        Text: FG,

        Keyword: HUE3,
        Keyword.Constant: HUE6,
        # Keyword.Declaration: None,
        Keyword.Namespace: HUE3,
        # Keyword.Pseudo: None,
        # Keyword.Reserved: None,
        Keyword.Type: HUE1,

        Name: MONO1,
        Name.Attribute: HUE6,
        Name.Builtin: HUE2,
        Name.Builtin.Pseudo: HUE6,
        Name.Class: HUE62,
        Name.Constant: HUE6,
        Name.Decorator: HUE2,
        # Name.Entity: None,
        Name.Exception: HUE2,
        Name.Function: HUE2,
        Name.Function.Magic: HUE1,
        Name.Label: HUE6,
        # Name.Namespace: None,
        # Name.Other: None,
        Name.Tag: HUE5,
        Name.Variable: HUE5,

        Literal: HUE6,
        String: HUE4,
        # String.Affix: None,
        # String.Backtick: None,
        # String.Char: None,
        # String.Delimiter: None,
        # String.Doc: None,
        # String.Double: None,
        String.Escape: HUE1,
        # String.Heredoc: None,
        # String.Interpol: None,
        # String.Other: None,
        # String.Regex: None,
        # String.Single: None,
        # String.Symbol: None,

        Number: HUE6,
        # Number.Bin: None,
        # Number.Float: None,
        # Number.Hex: None,
        # Number.Integer: None,
        # Number.Integer.Long: None,
        # Number.Oct: None,

        Operator: MONO1,
        Operator.Word: HUE3,

        Punctuation: MONO1,

        Comment: f'italic {MONO3}',
        # Comment.Hashbang: None,
        # Comment.Multiline: None,
        # Comment.Preproc: None,
        # Comment.Single: None,
        Comment.Special: HUE3,

        Generic: FG,
        Generic.Deleted: MONO3,
        Generic.Emph: f'italic {FG}',
        Generic.Error: HUE5,
        Generic.Heading: f'bold {FG}',
        # Generic.Inserted: None,
        # Generic.Output: None,
        # Generic.Prompt: None,
        Generic.Strong: f'bold {FG}',
        # Generic.Subheading: None,
        Generic.Traceback: f'italic {HUE6}',
    }

