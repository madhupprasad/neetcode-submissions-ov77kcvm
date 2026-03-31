class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        left = [-1]*n
        right = [n]*n
        st = [0]
        for i in range(1,n):
            while st and heights[st[-1]] >= heights[i]:
                st.pop()
            if st:
                left[i] = st[-1]
            st.append(i)
        st = []
        for i in range(n-1,-1,-1):
            while st and heights[st[-1]] >= heights[i]:
                st.pop()
            if st:
                right[i] = st[-1]
            st.append(i)
        
        m_area = 0
        for i in range(n):
            left[i]+=1
            right[i]-=1
            m_area = max(m_area, heights[i] * (right[i] - left[i] + 1))
        
        return m_area
            