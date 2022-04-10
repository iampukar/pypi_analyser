import requests
import warnings
from bs4 import BeautifulSoup
warnings.filterwarnings("ignore", category=UserWarning)

class pypi_analyser:
    
    def __init__(self, package_name):
        self.package_name = package_name
        if self._get_package_sanity() == False:
            raise SystemExit('PyPi Package not found!')
        if self._get_package_sanity2() == False:
            raise SystemExit('Package not found at libraries.io!')
        
        self.description = self._description()
        self.latest_version = self._latest_version()
        self.released = self._released()
        self.latest_release = self._latest_release()
        self.license = self._license()
        self.author = self._author()
        self.maintainer = self._maintainer()

        self.homepage = self._homepage()
        self.repository = self._repository()
        self.stars = self._stars()
        self.forks = self._forks()
        self.dependency_count = self._dependency_count()
        self.dependencies = self._dependencies()
        
    def __setitem__(self, key, value):
        setattr(self, key, value)

    def __getitem__(self, key):
        return getattr(self, key)
    
    def __repr__(self):
        return "%s" % (self.url)

    def __str__(self):
        return "%s" % (self.url)
    
    def _get_package_sanity(self):
        package_status = requests.get(f"https://pypi.org/project/{self.package_name}/")
        return True if package_status.status_code == 200 else False
    
    def _get_package_sanity2(self):
        package_status = requests.get(f"https://libraries.io/pypi/{self.package_name}/")
        return True if package_status.status_code == 200 else False

    def _package_pypi_parcer(self):
        page = requests.get(f"https://pypi.org/project/{self.package_name}/")
        soup = BeautifulSoup(page.content, "html.parser")
        return soup
    
    def _package_libraries_parcer(self):
        page = requests.get(f"https://libraries.io/pypi/{self.package_name}/")
        soup = BeautifulSoup(page.content, "html.parser")
        return soup
    
    def pypi_json(self):
        return requests.get(f"https://pypi.org/pypi/{self.package_name}/json").json()
    
    def _description(self):
        soup = self._package_pypi_parcer()
        tag = soup.find("div", {"class":"package-description"})
        return tag.findNext('p').get_text().strip() or None
    
    def _latest_version(self):
        soup = self._package_pypi_parcer()
        try:
            tag = soup.find("h1", {"class":"package-header__name"}).get_text().strip()
            return str(tag).split(' ')[1]
        except:
            return None
            
    def _license(self):
        try:
            json = self.pypi_json()
            return json['info']['license']
        except:
            soup = self._package_pypi_parcer()
            tag = soup.find_all("p")
            for sub_tag in tag:
                content = sub_tag.get_text()
                if content.startswith('License'):
                    return ' '.join(sub_tag.get_text().split(' ')[1:])
        return None
            
    def _author(self):
        try:
            json = self.pypi_json()
            return json['info']['author']
        except:
            soup = self._package_pypi_parcer()
            tag = soup.find_all("p")
            for sub_tag in tag:
                content = sub_tag.get_text()
                if content.startswith('Author'):
                    return ' '.join(sub_tag.get_text().split(' ')[1:])
        return None
    
    def _maintainer(self):
        soup = self._package_pypi_parcer()
        tag = soup.find_all("h3")
        for sub_tag in tag:
            content = sub_tag.get_text()
            if content.startswith('Maintainers'):
                return ''.join(sub_tag.findNext().get_text().strip())
        
    def _latest_release(self):
        soup = self._package_pypi_parcer()
        tag = soup.find("p", {"class":"package-header__date"})
        return tag.findNext('time').get_text().strip()
    
    def _homepage(self):
        try:
            json = self.pypi_json()
            return json['info']['project_urls']['Homepage']
        except:
            soup = self._package_libraries_parcer()
            tag = soup.find("p", {"class":"project-links"})
            if tag.findNext('a').get_text().startswith('Homepage'):
                return tag.findNext('a').get('href')
            
    def _repository(self):
        soup = self._package_libraries_parcer()
        tag = soup.find("p", {"class":"project-links"})
        if tag.findNext('a').get_text().startswith('Repository'):
                return tag.findNext('a').get('href')
            
    def _stars(self):
        soup = self._package_libraries_parcer()
        tag = soup.find_all("dt")
        for sub_tag in tag:
            content = sub_tag.get_text()
            if content.strip().startswith('Stars'):
                return sub_tag.findNext().get_text().strip()
            
    def _forks(self):
        soup = self._package_libraries_parcer()
        tag = soup.find_all("dt")
        for sub_tag in tag:
            content = sub_tag.get_text()
            if content.strip().startswith('Forks'):
                return sub_tag.findNext().get_text().strip()
            
    def _released(self):
        soup = self._package_libraries_parcer()
        tag = soup.find_all("dt")
        for sub_tag in tag:
            content = sub_tag.get_text()
            if content.strip().startswith('First release'):
                return sub_tag.findNext().get_text().strip()
            
    def _dependency_count(self):
        soup = self._package_libraries_parcer()
        tag = soup.find_all("dt")
        for sub_tag in tag:
            content = sub_tag.get_text()
            if content.strip().startswith('Dependencies'):
                return sub_tag.findNext().get_text().strip()
            
    def _dependencies(self):
        json = self.pypi_json()
        try:
            depen_requires = json['info']['requires_dist']
            p_name = [l.split(' ')[0] for l in ','.join(depen_requires).split(',')]
            p_ver = [str(l.split('(')[1]).split(')')[0] for l in ','.join(depen_requires).split(',')]
            return [i + j for i, j in zip(p_name, p_ver)]
        except:
            return None

        
if __name__ == '__main__':
    pypi_analyser(package_name)          