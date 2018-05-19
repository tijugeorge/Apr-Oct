import java.util.*;


class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {
        List<Integer> list = new ArrayList<Integer>();
        if (nums1.length > nums2.length) {
            for (int i = 0; i < nums2.length; i++) {
                for (int j = 0; j < nums1.length; j++) {
                    if (nums1[j] == nums2[i]) {
                        list.add(nums1[j]);
                    }
                } 
            }
        } else {             
            for (int i = 0; i < nums1.length; i++) {
                for (int j = 0; j < nums2.length; j++) {
                    if (nums2[j] == nums1[i]) {
                        list.add(nums2[j]);
                    }
                } 
            }       
        }
        Set<Integer> uniquearray = new HashSet<>(list);
        int[] array = uniquearray.stream().mapToInt(i->i).toArray();
        return array;
    }
}
