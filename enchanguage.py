def code(text):
     transcript = {'A': 'ᔑ', 'B': 'ʖ', 'C': 'ᓵ', 'D': '↸',
     'E': 'ᒷ','F': '⎓', 'G': '⊣', 'H': '⍑', 'I': '╎',
     'J': '⋮','K': 'ꖌ', 'L': 'ꖎ', 'M': 'ᒲ', 'N': 'リ',
     'O': "𝙹",'P': '!¡', 'Q': 'ᑑ', 'R': '∷', 'S': 'ʖ',
     'T': 'ᓭ','U': 'ᑴ', 'V': '!!', 'W': '∴', 'X': '⨅',
     'Y': 'Σ','Z': '⎺', ' ': ' '}
     s = ""
     text = text.upper()
     for char in text :
          if char in transcript:
               s += transcript[char]
          else:
               s += char
     return s

def decode(text):
     transcript = {'ᔑ': 'A', 'ʖ': 'S', 'ᓵ': 'C', '↸': 'D',
     'ᒷ': 'E', '⎓': 'F', '⊣': 'G', '⍑': 'H', '╎': 'I',
     '⋮': 'J', 'ꖌ': 'K', 'ꖎ': 'L', 'ᒲ': 'M', 'リ': 'N',
     '𝙹': 'O', '!¡': 'P', 'ᑑ': 'Q', '∷': 'R', 'ᓭ': 'T',
     'ᑴ': 'U', '!!': 'V', '∴': 'W', '⨅': 'X', 'Σ': 'Y',
     '⎺': 'Z', ' ': ' '}
     s = ""
     for char in text :
          if char in transcript:
               s += transcript[char]
          else:
               s += char
     return s
