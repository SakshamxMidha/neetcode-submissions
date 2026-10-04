class Solution:
    def maxArea(self, h: List[int]) -> int:
        l = 0
        r = len(h) - 1
        m_area = 0

        while l < r:

            area = min(h[l], h[r]) * (r-l)
            m_area = max(m_area, area)

            if h[l] < h[r]:
                l += 1
            else:
                r -= 1

        return m_area


        