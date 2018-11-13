class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        results = set()
        for email in emails:
            local, domain = email.split("@")
            #print(local , domain)
            local = local[:local.index("+")].replace(".", "") if "+" in local else local.replace(".", "")
            results.add(local + "@" + domain)
        return len(results)
