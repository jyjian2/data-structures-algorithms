# python3
import sys

def build_lps(pattern):
    lps = [0] * len(pattern)
    l = 0
    i = 1
    while i < len(pattern):
        if pattern[i] == pattern[l]:
            lps[i] = l + 1
            l += 1
            i += 1
        else:
            if l == 0:
                lps[i] = 0
                i += 1
            else:
                l = lps[l-1]
    return lps

def find_pattern(pattern, text):
  """
  Find all the occurrences of the pattern in the text
  and return a list of all positions in the text
  where the pattern starts in the text.
  """
  i = 0
  j = 0
  res = []
  lps = build_lps(pattern)
  while j < len(text):
      if pattern[i] == text[j]:
          i += 1
          j += 1
      else:
          if i > 0:
              i = lps[i - 1]
          else:
              j += 1
      if i == len(pattern):
          res.append(j - len(pattern))
          i = lps[i - 1]

  return res


if __name__ == '__main__':
  pattern = sys.stdin.readline().strip()
  text = sys.stdin.readline().strip()
  result = find_pattern(pattern, text)
  print(" ".join(map(str, result)))

