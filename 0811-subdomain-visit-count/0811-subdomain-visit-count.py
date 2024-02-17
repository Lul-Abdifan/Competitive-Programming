class Solution:
        def subdomainVisits( self, cpdomains ):
            counter = {}

            for domain in cpdomains:
                 number,domain_names = domain.split()
                 number = int( number )

                 domain_name = domain_names.split(".")
                 for i in range(len(domain_name)):
                     domain = ".".join(domain_name[i:])
                     if domain in counter:
                         counter[domain] +=number
                     else:
                         counter[domain] = number

            return [f"{counter[num]} {num}" for num in counter]   
                  
        
        