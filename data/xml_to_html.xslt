<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE xsl:stylesheet [<!ENTITY mdash "&#8212;"> ]>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:output method="html" indent="yes" omit-xml-declaration="yes"/>
    <xsl:template match="/">
        <table border="1">
            <tr>
                <td>
                    <strong>Time</strong>
                </td>
                <td>
                    <strong>Subject</strong>
                </td>
                <td>
                    <strong>Teacher</strong>
                </td>
                <td>
                    <strong>Kind</strong>
                </td>
                <td>
                    <strong>Audience</strong>
                </td>
                <xsl:for-each select="timetable/dayOfWeek">
                    <tr>
                        <td colspan="5">
                            <strong>
                                <xsl:value-of select="@name"/>
                            </strong>
                        </td>
                    </tr>

                    <xsl:for-each select="subject">
                        <tr>
                            <td>
                                <xsl:value-of select="@start"/>
                                <xsl:text> &mdash; </xsl:text>
                                <xsl:value-of select="@end"/>
                            </td>
                            <td>
                                <xsl:value-of select="name"/>
                            </td>
                            <td>
                                <xsl:value-of select="lecturer"/>
                            </td>
                            <td>
                                <xsl:value-of select="kind"/>
                            </td>
                            <td>
                                <xsl:value-of select="auditory"/>
                            </td>
                        </tr>
                    </xsl:for-each>
                </xsl:for-each>
            </tr>
        </table>
    </xsl:template>
</xsl:stylesheet>