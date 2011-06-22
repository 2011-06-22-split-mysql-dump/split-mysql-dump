# -*- mode: python; coding: utf-8 -*-
#
# Copyright 2011 Andrej A Antonov <polymorphm@qmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

def split(filename):
    header = []
    out_fd = None
    sql_no = 0
    
    with open(filename) as in_fd:
        for line in in_fd:
            if line.startswith('-- Current Database: `') and line.endswith('`\n'):
                out_basename = line[len('-- Current Database: `'):-len('`\n')]
                out_filename = '{}-{}-{}.sql'.format(
                        filename, sql_no, out_basename)
                sql_no += 1
                out_fd = open(out_filename, 'w')
                
                for h_line in header:
                    out_fd.write('{}'.format(h_line))
                out_fd.write('{}'.format(line))
            else:
                if out_fd is not None:
                    out_fd.write('{}'.format(line))
                else:
                    header.append(line)
